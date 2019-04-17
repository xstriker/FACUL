import java.util.HashMap;

public class MapTester
{
    private HashMap<String, String> agenda;

    public MapTester()
    {
        this.agenda = new HashMap<String, String>();
    }

    public void enterNumber (String nome, String numero)
    {
        this.agenda.put(nome, numero);
    }
    
    public String lookupNumber (String nome)
    {
        return this.agenda.get(nome);
    }
}
