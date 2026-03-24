import java.util.Scanner;
/*public class assignment1 {
    public static void printDigits(int n){
        if(n == 0)
            return;
        printDigits(n/10);
        System.out.println(n%10);
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        printDigits(n);

    }
}*/

/*public class assignment1 {
    static int sum(int c, Scanner sc){
        if(c==0)
            return 0;
        int n =sc.nextInt();
        return n+sum(c-1, sc);
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        int total = sum(c, sc);
        double avg = (double) total/c;
        System.out.println(avg);
    }
}*/

/*public class assignment1{
    static boolean prime(int n, int i){
        if(i == 1)
          return true;
        if(n%i==0)
          return false;
        return prime(n,i-1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n <=1){
            System.out.println("Composite");
            return;
        }
        if(prime(n,n-1))
            System.out.println("Prime");
        else
            System.out.println("Composite");
    }
}*/
/*public class assignment1{
    static int fact(int n){
        if(n == 0 || n==1)
            return 1;
        return n * fact(n-1);
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fact(n));
    }
}*/

/*public class assignment1 {
    static int fib(int n){
        if(n == 0)
            return 0;
        if(n == 1)
            return 1;
        return fib(n-1)+fib(n-2);
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(fib(n));

    }
}*/

/*public class assignment1 {
    static int power(int a, int n){
        if(n == 0)
            return 1;
        return a*power(a, n-1);
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a=sc.nextInt();
        int n=sc.nextInt();
        System.out.println(power(a,n));
    }
}*/

/*public class assignment1 {
    static void reverse(int n, Scanner sc){
        if(n == 0)
            return;
        int x = sc.nextInt();
        reverse(n-1, sc);
        System.out.print(x+" ");
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        reverse(n,sc);
    }
}*/

/*public class assignment1 {
    static boolean check(String s, int i){
        if(i == s.length())
            return true;
        if(!Character.isDigit(s.charAt(i)))
            return false;
        return check(s, i+1);
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        if(check(s,0))
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}*/

/*public class assignment1 {
    static int count(String s){
        if(s.equals(""))
            return 0;
        return 1 + count(s.substring(1));
    }
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        String s =sc.nextLine();
        System.out.println(count(s));
    }
}*/

public class assignment1 {
    static int gcd(int a, int b){
        if(b == 0)
            return a;
        return gcd(b, a % b);
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(gcd(a,b));
    }
}