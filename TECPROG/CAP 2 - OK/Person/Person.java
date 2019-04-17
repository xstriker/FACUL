public class Person
{
    private int age;
    private String name;
    
    public Person(int age, String name)
    {
        this.age = age;
        this.name = name;
    }
    
    public void printDetails()
    {
        System.out.println("The name of this person is" + this.name + " and he's/she's " + age + "years old");
    }
    
    public void setAge(int age) {
        this.age = age;
    }
}
