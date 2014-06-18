import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;


public class ListaCanciones {

	/**
	 * 	Usando la clase Cancion
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		File archivo = null;
		FileReader fr = null;
		BufferedReader br = null;
		
		Cancion canciones[] = new Cancion[13];
		
		try {
			archivo = new File("Wrecking_Ball.csv");
			fr = new FileReader(archivo);
			br = new BufferedReader(fr);
			
			String datos[]; //array almacenar cadena
			String linea; //almacenar lineas
			
			
			int nlinea = 0;
			
			while((linea = br.readLine()) != null){
				
				if (nlinea > 0){
					datos = linea.split(";");
					Cancion cn = new Cancion(datos[0].trim(), datos[1].trim(), datos[2].trim());
					canciones[nlinea -1] = cn;
				}
				
				nlinea++;
			}
			
			
		} catch (Exception e) {
			System.out.println("No se puede leer el fichero Wrecking_Ball.csv");
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
		
		for (int i=0; i<12; i++){
			System.out.println(canciones[i].toString());
		}
		
		
		
	}

}
