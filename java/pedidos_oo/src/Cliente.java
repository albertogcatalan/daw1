
public class Cliente {
	private String cif;
	private String razonsocial;
	private String domiciliosocial;
	private String codpostal;
	private String poblacion;
	private String provincia;
	private String telefono;
	private Float creditlimite;
	
	
	
	public Cliente(String cif, String razonsocial, String domiciliosocial,
			String codpostal, String poblacion, String provincia,
			String telefono, Float creditlimite) {
		
		this.cif = cif;
		this.razonsocial = razonsocial;
		this.domiciliosocial = domiciliosocial;
		this.codpostal = codpostal;
		this.poblacion = poblacion;
		this.provincia = provincia;
		this.telefono = telefono;
		this.creditlimite = creditlimite;
	}
	
	public Cliente()
	{
	}
	
	public String getCif() {
		return cif;
	}
	public void setCif(String cif) {
		this.cif = cif;
	}
	public String getRazonsocial() {
		return razonsocial;
	}
	public void setRazonsocial(String razonsocial) {
		this.razonsocial = razonsocial;
	}
	public String getDomiciliosocial() {
		return domiciliosocial;
	}
	public void setDomiciliosocial(String domiciliosocial) {
		this.domiciliosocial = domiciliosocial;
	}
	public String getCodpostal() {
		return codpostal;
	}
	public void setCodpostal(String codpostal) {
		this.codpostal = codpostal;
	}
	public String getPoblacion() {
		return poblacion;
	}
	public void setPoblacion(String poblacion) {
		this.poblacion = poblacion;
	}
	public String getProvincia() {
		return provincia;
	}
	public void setProvincia(String provincia) {
		this.provincia = provincia;
	}
	public String getTelefono() {
		return telefono;
	}
	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}
	public Float getCreditlimite() {
		return creditlimite;
	}
	public void setCreditlimite(Float creditlimite) {
		this.creditlimite = creditlimite;
	}
	

	
}
