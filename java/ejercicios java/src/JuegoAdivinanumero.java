
import java.util.Scanner;

public class JuegoAdivinanumero {
	static public void main(String[] args){
		
		int x = (int) (100*Math.random()+1);
		int numero, min, max;
		int intentos = 5;
		
		Scanner in = new Scanner(System.in);
		System.out.println("num: "+x);
		
		min = 1;
		max = 100;
		
		do {
			if (intentos >= 1){
				
				System.out.println("Introduce un numero entre " + min + " y " + max);
				numero = in.nextInt();
				if (x < numero){
					max = x - 1;
					System.out.println("numero oculto es menor");
					intentos = intentos - 1;
				}else if (x > numero){
					min = x + 1;
					System.out.println("numero oculto es mayor");
					intentos = intentos - 1;
				}else {
					System.out.println("has adivinado el numero");
				}
				
			}else {
				System.out.println("has perdido");
			}
			
		} while (oculto != numero && veces < 5);
		
		// por quŽ ha salido del bucle?
		
		if (numero )
	}

}
