public class MyPetDog{
    public string name;
    public string breed;
    public int age;

    public MyPetDog(string name, string breed, int age){
        this.name = name;
        this.breed = breed;
        this.age = age;
    }
    public MyPetDog(){
        this(“Fido”,”golden retriever”, 1);
    }

    public void bark(){
        System.out.println(“woof”);
    }
    public static void main(String[] args){
        MyPetDog Cas = new MyPetDog(“Cas”,”cockerspaniel”,6);
        System.out.println(Cas.age);
        Cas.bark();
    }
}
