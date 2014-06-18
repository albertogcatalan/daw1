
public class Cancion {
	
	public String titulo;
	public String autor;
	public int duracion;
	
	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	public String getAutor() {
		return autor;
	}
	public void setAutor(String autor) {
		this.autor = autor;
	}
	public int getDuracion() {
		return duracion;
	}
	public void setDuracion(int duracion) {
		this.duracion = duracion;
	}
	
	public Cancion(String autor, String titulo, int duracion){
		this.titulo = titulo;
		this.autor = autor;
		this.duracion = duracion;
	}
	
	public Cancion(String autor, String titulo, String duracion){
		this(autor, titulo, aSegundos(duracion));
	}
	
	public static int aSegundos(String dura){
		//convertir minutos:segundos a segundos
		String [] min_seg = dura.split(":");
        return Integer.parseInt(min_seg[0].trim())*60 + Integer.parseInt(min_seg[1].trim());
	}
	
	public String toString(){
		return titulo + " [" + autor + "] " + duracion + "\"";
	}

}
