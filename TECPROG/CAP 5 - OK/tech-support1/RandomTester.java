import java.util.Random;

public class RandomTester
{
    Random gerador;
    
    public RandomTester() {
        this.gerador = new Random();
    }
    
    public void printOneRandom() {
        System.out.println(gerador.nextInt());
    }
    
    public void printMultiRandom(int y)
    {
        for(int i = 0; i<y; i++) {
            this.printOneRandom();
        }
    }
}
