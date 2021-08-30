import java.util.ArrayList;
import java.util.Scanner;
import java.time.LocalTime;
import java.time.LocalDate;

class Utility {
    public static final Scanner SCANNER = new Scanner(System.in);
}
class Door{
    public void entrance(){
        System.out.println("Welcome to our zoo! You are very lucky to see the most beautiful animals in the world. We wish you all a nice day. Have fun.");
    }
}
class Fee{
    public void pay(){
        System.out.println("You paid 10 dollars.");
    }
}
class List{
    public void pls(){
        ArrayList<String> animalss = new ArrayList<String>();
        animalss.add("Lion");
        animalss.add("Tiger");
        animalss.add("Crocodile");
        animalss.add("Snake");
        animalss.add("Hamsi");
        animalss.add("Shark");
        animalss.add("Giraffe");
        animalss.add("Penguin");
        for(int i=0;i < animalss.size();i++){
            System.out.println(animalss.get(i));

        }
        System.out.println("If you visit with staff. You can learn more things about our animals... another time. ");
    }
}

class Time{
    public void time(){
        LocalTime hour = LocalTime.now();
        System.out.println("Time: "+ hour);
        LocalDate date = LocalDate.now();
        System.out.println("Date: "+ date);
    }
}

interface Flying{
    public void variety();
    public void age();
    public void name();
    public void fly();

}
class Parrot implements Flying{
    public void variety(){
        System.out.println("Parrot");

    }
    public void age(){
        System.out.println(12);
    }
    public void name(){
        System.out.println("Rick");
    }
    public void fly(){
        System.out.println("It can fly");
    }
}
class Penguin implements Flying{
    public void variety(){
        System.out.println("Penguin");

    }
    public void age(){
        System.out.println(11);
    }
    public void name(){
        System.out.println("Jessy");
    }
    public void fly(){
        System.out.println("It can't fly");
    }
}
class Felidae {//(Cat family)
    String variety;
    int age;
    String name;

    public Felidae(String avariety,int aage, String aname){
    variety = avariety;
    age = aage;
    name = aname;
}
}
class Reptile {
    String variety;
    int age;
    String name;

    public Reptile(String bvariety,int bage, String bname){
    variety = bvariety;
    age = bage;
    name = bname;

}
}
class Fish {
    String variety;
    int age;
    String name;

    public Fish(String cvariety,int cage, String cname){
    variety = cvariety;
    age = cage;
    name = cname;

}
}
class Giraffe{
    public void giraffe(){
        System.out.println("We have a giraffe. He is 13 years old and his name is mike.");
    }
}
class Feeding {
    public void animalss(){
        System.out.println("All animals are praying for you. Thank you so much giving food to them. You are a nice person...");
    }
}
class BadPerson {
    public void humanity(){
        System.out.println("You are a bad man or poor. If you are not poor and doing this then fuck you...");
    }
}
public class Zoo{

    public static void main(String[] args) {
        Fee fee = new Fee();
        List animallist = new List();
        Felidae lion = new Felidae("Lion",10,"Jake");
        Felidae tiger = new Felidae("Tiger", 8, "Benjamin");
        Reptile crocodile = new Reptile("Crocodile", 32, "Jim");
        Reptile snake = new Reptile("Snake", 9, "Lily");
        Fish hamsi = new Fish("Hamsi", 1, "Temel");
        Fish shark = new Fish("Shark", 17, "John");
        
        Giraffe watch = new Giraffe();
        Penguin penguin = new Penguin();
        Parrot parrot = new Parrot();
        Feeding feed = new Feeding();
        BadPerson bad = new BadPerson();
        
        Flying[] flyers = new Flying[2];
        flyers[0] = penguin;
        flyers[1] = parrot;
        Door go = new Door();
        Time look = new Time();
        
        look.time();
        fee.pay();
        go.entrance();
        
        System.out.println("If you want to visit our zoo with the help of our staff, write 1, if you want to visit alone, write 2");
        int answer = Utility.SCANNER.nextInt();
        
        System.out.println("It looks like you chose "+ answer);
        if(answer==1){
            watch.giraffe();
            System.out.println("We have a "+ lion.variety+". It is "+ lion.age+" years old. His name is "+ lion.name);
            System.out.println("We have a "+ tiger.variety+". It is "+ tiger.age+" years old. His name is "+ tiger.name);
            System.out.println("We have a "+ crocodile.variety+". It is "+ crocodile.age+" years old. His name is "+ crocodile.name);
            System.out.println("We have a "+ snake.variety+". It is "+ snake.age+" years old. His name is "+ snake.name);
            System.out.println("We have a "+ hamsi.variety+". It is "+ hamsi.age+" years old. His name is "+ hamsi.name);
            System.out.println("We have a "+ shark.variety+". It is "+ shark.age+" years old. His name is "+ shark.name);
            System.out.println("Infos of our flyers:");
            for(Flying flyer : flyers){
                flyer.variety();
                flyer.age();
                flyer.name();
                flyer.fly();
            }
            System.out.println("Do you want to feed them? type 1/2");
            int answerr = Utility.SCANNER.nextInt();
            if(answerr == 1){
                feed.animalss();
            }
            else if(answerr==2){
                bad.humanity();
                


            }
            else{
                System.out.println("Probably u entered wrong something... We wish u a nice life. Thank u for visiting us again bye.");
            }
            System.out.println("We wish u a nice life. Thank u for visiting us again. We want to see you again at the future. Bye bye brother...");

        }
        else if(answer==2){
            System.out.println("Have a nice visiting...");
            animallist.pls();
            
        }
        else{
            System.out.println("Looks like u entered wrong. Please run again...");
        }
        
        
    }

}
