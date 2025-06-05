import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Storage } from '@ionic/storage-angular';
import { IonHeader, IonToolbar, IonTitle, IonContent, LoadingController, NavController, ToastController, IonButton, IonList, IonItem, IonInput, AlertController} from '@ionic/angular/standalone';

import { addIcons } from 'ionicons'; 
import { businessOutline, cameraOutline, trailSignOutline, } from 'ionicons/icons';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  imports: [IonList, IonItem, IonInput, IonButton, IonContent, FormsModule],
  providers: [Storage]
})
export class HomePage {

  constructor(
    public contole_carreregamento: LoadingController,
    public controle_navegacao: NavController,
    public controle_alerta: AlertController,
    public controle_toast: ToastController,
    public storage: Storage
  ) {}

  async ng0nInit() {
    await this.storage.create();
  }

  public instancia:{username: string, password: string} = {
    username: '',
    password: ''
  };

  async autenticarUsuario() {
    alert('Teste');
  }
}