import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./home/home.page').then((m) => m.HomePage),
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },
  {
    path: 'veiculo',
    loadComponent: () => import('./veiculo/veiculo.page').then( m => m.VeiculoPage)
  },
];
