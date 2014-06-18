
public class Cliente {
	private String nombre;
	private String CIF;

	public String getCIF() {
		return CIF;
	}

	public void setCIF(String cIF) {
		CIF = cIF;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	@Override
	public String toString() {
		return nombre + " [" + CIF + "]";
	}

	public Cliente(String nombre, String cIF) {
		super();
		this.nombre = nombre;
		CIF = cIF;
	}
	
	
}
