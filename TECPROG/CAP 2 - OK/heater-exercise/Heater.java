
/**
 * Escreva a descrição da classe Heater aqui.
 * 
 * @author (seu nome) 
 * @version (número de versão ou data)
 */
public class Heater
{
    private int temperature;
    private int min;
    private int max;
    private int increment;

    /**
     * COnstrutor para objetos da classe Heater
     */
    public Heater(int min, int max)
    {
        this.min = min;
        this.max = max;
        this.increment = 5;
        this.temperature = 15;
    }
    
    public void warmer()
    {
        if(this.temperature + this.increment <= this.max) {
            this.temperature += this.increment;
        }
    }
    
    public void cooler()
    {
        if(this.temperature - this.increment >= this.min) {
            this.temperature -= this.increment;
        }
    }
    
    public int getTemp() {
        return this.temperature;
    }
    
    public void setIncrement(int inc) {
        if(inc >= 0) {
            this.increment = inc;
        }
    }
}
