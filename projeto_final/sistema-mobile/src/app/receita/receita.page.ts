import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, LoadingController, NavController, ToastController, IonButtons, IonMenuButton, IonText, IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent, IonList, IonItem, IonItemSliding, IonThumbnail, IonLabel, IonItemOptions, IonItemOption, IonButton, IonIcon, IonBadge } from '@ionic/angular/standalone';
import { Storage } from '@ionic/storage-angular';
import { Receita } from './receita.model';
import { Usuario } from '../home/usuario.model';
import { CapacitorHttp, HttpOptions, HttpResponse } from '@capacitor/core';

@Component({
  standalone: true,
  selector: 'app-receita',
  templateUrl: './receita.page.html',
  styleUrls: ['./receita.page.scss'],
  imports: [IonItemOption, IonItemOptions, IonLabel, IonItemSliding, IonItem, IonList, IonCardContent, IonCardSubtitle, IonCardTitle, IonCardHeader, IonCard, IonButtons, IonMenuButton, IonContent, IonHeader, IonToolbar, IonThumbnail, CommonModule, FormsModule],
  providers: [Storage]
})
export class ReceitaPage implements OnInit {

  public usuario: Usuario = new Usuario();
  public lista_receitas: Receita[] = [];

  constructor(
    public storage: Storage,
    public controle_toast: ToastController,
    public controle_navegacao: NavController,
    public controle_carregamento: LoadingController
  ) { }

  async ngOnInit() {

    // Verifica se existe registro de configuração para o último usuário autenticado
    await this.storage.create();
    const registro = await this.storage.get('usuario');

    if(registro) {
      this.usuario = Object.assign(new Usuario(), registro);
      this.consultarReceitasSistemaWeb();
    }
    else{
      this.controle_navegacao.navigateRoot('/home');
    }
  }

  async consultarReceitasSistemaWeb() {

    // Inicializa interface com efeito de carregamento
    const loading = await this.controle_carregamento.create({message: 'Pesquisando...', duration: 60000});
    await loading.present();

    // Define informações do cabeçalho da requisição
    const options: HttpOptions = {
      headers: {
        'Content-Type': 'application/json',
        'Authorization':`Token ${this.usuario.token}`
      },
      url: 'http://127.0.0.1:8000/receita/api/'
    };

    CapacitorHttp.get(options)
      .then(async (resposta: HttpResponse) => {

        // Verifica se a requisição foi processada com sucesso
        if(resposta.status == 200) {
          this.lista_receitas = resposta.data;
        
          // Finaliza interface com efeito de carregamento
          loading.dismiss();
        }
        else {

          // Finaliza autenticação e apresenta mensagem de erro
          loading.dismiss();
          this.apresenta_mensagem(`Falha ao consultar receitas: código ${resposta.status}`);
        }
      })
      .catch(async (erro: any) => {
        console.log(erro);
        loading.dismiss();
        this.apresenta_mensagem(`Falha ao consultar receitas: código ${erro?.status}`);
      });
  }

  async excluirReceita(id: number) {

    // Inicializa interface com efeito de carregamento
    const loading = await this.controle_carregamento.create({message: 'Autenticando...', duration: 30000});
    await loading.present();

    const options: HttpOptions = {
      headers: {
        'Content-Type': 'application/json',
        'Authorization':`Token ${this.usuario.token}`
      },
      url: `http://127.0.0.1:8000/receita/api/${id}/`
    };

    CapacitorHttp.delete(options)
      .then(async (resposta: HttpResponse) => {

        // Verifica se a requisição foi processada com sucesso
        if(resposta.status == 200) {
        
          // Finaliza interface com efeito de carregamento
          loading.dismiss();

          // Consulta novamente a lista de veículos
          this.consultarReceitasSistemaWeb();
        }
        else {

          // Finaliza autenticação e apresenta mensagem de erro
          loading.dismiss();
          this.apresenta_mensagem(`Falha ao excluir o receita: código ${resposta.status}`);
        }
      })
      .catch(async (erro: any) => {
        console.log(erro);
        loading.dismiss();
        this.apresenta_mensagem(`Falha ao excluir o receita: código ${erro?.status}`);
      });
  }

  async apresenta_mensagem(texto: string) {
    const mensagem = await this.controle_toast.create({
      message: texto,
      cssClass: 'ion-text-center',
      duration: 2000
    });
    mensagem.present();
  }
}


