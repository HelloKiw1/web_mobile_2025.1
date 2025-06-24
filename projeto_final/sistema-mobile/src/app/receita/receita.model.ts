export class Receita {
    // Atributos da classe Receita
  public id: number;
  public nome: string | null;
  public tipo: number | null;         // small integer com choices
  public gosto: number | null;        // small integer com choices
  public tempo_preparo: string | null; // Django DurationField → string (ex: "00:30:00")
  public porcoes: number | null;
  public dificuldade: number | null;  // small integer com choices
  public ingredientes: string | null;
  public receita: string | null;
  public foto: string | null;         // imagem (URL ou base64 ou path relativo)

  constructor() {
    this.id = 0;
    this.nome = null;
    this.tipo = null;
    this.gosto = null;
    this.tempo_preparo = null;
    this.porcoes = null;
    this.dificuldade = null;
    this.ingredientes = null;
    this.receita = null;
    this.foto = null;
  }
}
