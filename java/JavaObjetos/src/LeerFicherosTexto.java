import java.io.*;

public class LeerFicherosTexto {
	
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
		File archivo = null;
		FileReader fr = null;
		BufferedReader br = null;
		
		try {
			archivo = new File("datos.txt");
			fr = new FileReader(archivo);
			br = new BufferedReader(fr);
			
			String linea;
			while((linea = br.readLine()) != null){
				String empleado = linea.substring(0,7);
				Integer horas = Integer.parseInt(linea.substring(8,11).trim());
				Integer precioHora = Integer.parseInt(linea.substring(12).trim());
				System.out.println("-----------------------");
				System.out.println("C—digo empleado: " + empleado);
				System.out.println("Horas: " + horas);
				System.out.println("Precio hora: " + precioHora + "Û");
				System.out.println("Salario total: " + sueldoNeto(horas, precioHora) + "Û");
			}
			
		} catch (Exception e) {
			System.out.println("No se puede leer el fichero datos.txt");
		}
		
		finally{
			if (fr != null){
				try {
					fr.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
		}

	}

}
