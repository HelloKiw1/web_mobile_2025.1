import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReceitaPage } from './receita.page';

describe('VReceitaPage', () => {
  let component: ReceitaPage;
  let fixture: ComponentFixture<ReceitaPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(ReceitaPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

