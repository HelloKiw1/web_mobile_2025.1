export class Veiculo
{
    public id: number;
    public marca: number;
    public nome_marca: string;
    public modelo: string;
    public ano: number;
    public cor: number;
    public nome_cor: string;
    public foto: string | undefined;
    public combustivel: number;
    public nome_combustivel: string;

    constructor() {
        this.id = 0;
        this.marca = 0;
        this.nome_marca = '';
        this.modelo = '';
        this.ano = 0;
        this.cor = 0;
        this.nome_cor = '';
        this.combustivel = 0;
        this.nome_combustivel = '';
    }

  }

