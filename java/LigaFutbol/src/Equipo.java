
public class Equipo {
	public String nombre;
	public int pganados = 0;
	public int pempatados = 0;
	
	public String getName() {
		return nombre;
	}
	
	public String toString(){
		return nombre + " (" + puntos() + ")";
	}
	
	public Equipo(String eq, int gana, int empata){
		nombre = eq;
		pganados = gana;
		pempatados = empata;
	}
	
	public Equipo(String eq, String gana, String empata){
		nombre = eq;
		pganados = Integer.parseInt(gana);
		pempatados = Integer.parseInt(empata);
	}
	
	
	public int puntos(){
		return pganados * 3 + pempatados;
		
	}
}
