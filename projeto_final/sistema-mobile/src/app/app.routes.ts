import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./home/home.page').then((m) => m.HomePage),
  },
  {
    path: '',
    redirectTo: 'receita',
    pathMatch: 'full',
  },{
    path: 'receita',
    loadComponent: () => import('./receita/receita.page').then( m => m.ReceitaPage)
  },
];
