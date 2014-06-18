import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;


public class EjecutaLiga {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		File archivo = null;
		FileReader fr = null;
		BufferedReader br = null;
		
		Equipo equipos[] = new Equipo[20];
		
		try {
			archivo = new File("ligahoy.csv");
			fr = new FileReader(archivo);
			br = new BufferedReader(fr);
			
			String datos[]; //array almacenar cadena
			String linea; //almacenar lineas
			
			
			int nlinea = 0;
			
			while((linea = br.readLine()) != null){
				
				if (nlinea > 0){
					datos = linea.split(";");
					Equipo eq = new Equipo(datos[1], datos[3], datos[4]);
					equipos[nlinea -1] = eq;
				}
				
				nlinea++;
			}
			
			
		} catch (Exception e) {
			System.out.println("No se puede leer el fichero ligahoy.csv");
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
		
		//mostrar ordenado mayor a menor
		Arrays.sort(equipos, new Comparator(){
			public int compare(Object o1, Object o2){
				String nombre1 = ((Equipo) o1).getName();
				String nombre2 = ((Equipo) o2).getName();
				return nombre1.compareTo(nombre2);
			}
		});
		
		//mostrar ordenado menor a mayor
		Arrays.sort(equipos, new Comparator(){
			public int compare(Object o1, Object o2){
				String nombre1 = ((Equipo) o1).getName();
				String nombre2 = ((Equipo) o2).getName();
				return nombre2.compareTo(nombre1);
			}
		});
				
		//mostrar ordenado por puntos
		Arrays.sort(equipos, new Comparator(){
			public int compare(Object o1, Object o2){
				int puntos1 = ((Equipo) o1).puntos();
				int puntos2 = ((Equipo) o2).puntos();
				if (puntos1 < puntos2){
					return -1; //el primero es menor
				}else if(puntos2 < puntos1){
					return 1; // el segundo menor
				}else{
					return 0; //iguales
				}
			}
		});
		
		for (int i=0; i<20; i++){
			System.out.println(equipos[i].toString());
		}
	}
}
