

public class Main {

    static class Human {
        protected int age;
        protected String name;

        Human (){

        }

        static void humanVoice(Human human){

            System.out.println("Voice:");

            if (human instanceof Man){
                System.out.println(((Man)human).voice());
            } else if (human instanceof Woman){
                System.out.println(((Woman)human).voice());
            }
            else {
                System.out.println("Unknown!");
            }
        }

        
    }

    static class Man extends Human {

        public Man (String name, int age){
            super();
            this.name = name;
            this.age = age;
        }

        public String getName(){
            return this.name;
        }

        public void setName(String name){
            this.name = name;
        }

        public int getAge(){
            return this.age;
        }

        public void setAge(){
            this.age = age;
        }

        public String voice(){
            return "I'm a man!";
        }
    }

    static class Woman extends Human {

        public Woman (String name, int age){
            super();
            this.name = name;
            this.age = age;
        }

        public String getName(){
            return this.name;
        }

        public void setName(String name){
            this.name = name;
        }

        public int getAge(){
            return this.age;
        }

        public void setAge(){
            this.age = age;
        }

        public String voice(){
            return "I'm a woman!";
        }
    }


    public static void main(String[] args){
        Human human1 = new Man ("Sam", 21);
        System.out.println(((Man)human1).getName());
        System.out.println(((Man)human1).getAge());
        System.out.println(((Man)human1).voice());

        Human human2 = new Woman ("Jeni", 20);
        System.out.println(((Woman)human2).getName());
        System.out.println(((Woman)human2).getAge());
        System.out.println(((Woman)human2).voice());

        Human.humanVoice(human1);
        Human.humanVoice(human2);
    }
}