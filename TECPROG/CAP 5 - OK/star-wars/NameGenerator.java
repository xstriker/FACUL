public class NameGenerator
{
    private String nome;
    private String sobrenome;
    private String sobrenomeMae;
    private String cidade;

    public NameGenerator(String nome, String sobrenome, String sobrenomeMae, String cidade)
    {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.sobrenomeMae = sobrenomeMae;
        this.cidade = cidade;
    }
    
    public String generateStarWarsName()
    {
        return this.sobrenome.substring(0, 3) + this.nome.substring(0, 2).toLowerCase() + " " + this.sobrenomeMae.substring(0, 2) + this.cidade.substring(0, 3).toLowerCase();
    }
}
