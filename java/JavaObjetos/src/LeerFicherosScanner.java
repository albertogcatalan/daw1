import java.io.*;
import java.util.Scanner;

public class LeerFicherosScanner {
	
	public static int sueldoNeto(int horas, int precioHora){
		/*las horas mensuales obligatorias de trabajo son 140
		las horas por encima de 140 se consideran horas extras
		las horas extras se pagan al 65 % m‡s que las horas ordinarias
		si el salario bruto es mayor que 2000 euros, se aplica una deducci—n por impuestos del 12 %; si no, no se aplica deducci—n alguna
		*/
		double salarioBruto = 0;
		if (horas > 140){
			int horasExtras = horas - 140;
			double precioExtras = precioHora * 1.65;
			double horasExtrasTotales = horasExtras * precioExtras;
			salarioBruto = horasExtrasTotales + (precioHora * 140);
		}else{
			salarioBruto = precioHora * 140;
		}
		
		if (salarioBruto > 2000){
			return (int) (salarioBruto * 0.88);
		} else{
			return (int) salarioBruto;
		}
		
	}
	
	/**
	 * Ejemplos de lectura de ficheros de texto
	 */
	public static void main(String[] args) {
		Scanner datos = null;
		
		try {
			
			File f = new File("datos.txt");
			datos = new Scanner(f);
			
			while (datos.hasNext()){
				String empleado = datos.next();
				Integer horas = Integer.parseInt(datos.next());
				Integer precioHora = Integer.parseInt(datos.next());
				System.out.println("-----------------------");
				System.out.println("Empleado: " + empleado);
				System.out.println("Horas: " + horas);
				System.out.println("Precio hora: " + precioHora + "Û");
				System.out.println("Salario total: " + sueldoNeto(horas, precioHora) + "Û");
			}
			
		} catch (Exception e) {
			System.out.println("No se puede leer el fichero datos.txt");
		}

	}

}