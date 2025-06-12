import { ComponentFixture, TestBed } from '@angular/core/testing';
import { VeiculoPage } from './veiculo.page';

describe('VeiculoPage', () => {
  let component: VeiculoPage;
  let fixture: ComponentFixture<VeiculoPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(VeiculoPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

