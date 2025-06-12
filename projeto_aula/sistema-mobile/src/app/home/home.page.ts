import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Storage } from '@ionic/storage-angular';
import { CapacitorHttp, HttpOptions, HttpResponse } from '@capacitor/core';
import { IonContent, LoadingController, NavController, AlertController, ToastController, IonItem, IonInput, IonButton } from '@ionic/angular/standalone';
import { Usuario } from './usuario.model';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  imports: [IonItem, IonInput, IonButton, IonContent, FormsModule],
  providers: [Storage]
})
export class HomePage {
  
  constructor(
    public controle_carregamento: LoadingController,
    public controle_navegacao: NavController,
    public controle_alerta: AlertController,
    public controle_toast: ToastController,
    public storage: Storage
  ) {}

  async ngOnInit() {
    await this.storage.create();
  }

  public instancia: { username: string, password: string } = {
    username: '',
    password: ''
  };

  async autenticarUsuario() {

    // Inicializa interface com efeito de carregamento
    const loading = await this.controle_carregamento.create({message: 'Autenticando...', duration: 15000});
    await loading.present();

    // Define informações do cabeçalho da requisição
    const options: HttpOptions = {
      headers: {'Content-Type': 'application/json'},
      url: 'http://127.0.0.1:8000/autenticacao-api/',
      data: this.instancia
    };

    // Autentica usuário junto a API do sistema web
    CapacitorHttp.post(options)
      .then(async (resposta: HttpResponse) => {

        // Verifica se a requisição foi processada com sucesso
        if(resposta.status == 200) {
          
          // Armazena localmente as credenciais de usuário
          let usuario: Usuario = Object.assign(new Usuario(), resposta.data);
          await this.storage.set('usuario', usuario);
          
          // Finaliza autenticação e redireciona para interface inicial
          loading.dismiss();
          this.controle_navegacao.navigateRoot('/veiculo');
        }
        else {

          // Finaliza autenticação e apresenta mensagem de erro
          loading.dismiss();
          this.apresenta_mensagem(resposta.status);
        }
      })
      .catch(async (erro: any) => {
        console.log(erro);
        loading.dismiss();
        this.apresenta_mensagem(erro?.status);
      });
  }

  async apresenta_mensagem(codigo: number) {
    const mensagem = await this.controle_toast.create({
      message: `Falha ao autenticar usuário: código ${codigo}`,
      cssClass: 'ion-text-center',
      duration: 2000
    });
    mensagem.present();
  }
}