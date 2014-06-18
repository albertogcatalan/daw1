import java.util.Date;

public class Trabajador
{
	// Para las fechas
  private String nombre;
  private String puesto;
  private String direccion;
  
  //Métodos get & set
  public String getNombre() {
	return nombre;
  }
  
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getPuesto() {
		return puesto;
	}
	public void setPuesto(String puesto) {
		this.puesto = puesto;
	}
	public String getDireccion() {
		return direccion;
	}
	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}
	public String getTelefono() {
		return telefono;
	}
	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}
	public Date getFecha_nacimiento() {
		return fecha_nacimiento;
	}
	public void setFecha_nacimiento(Date fecha_nacimiento) {
		this.fecha_nacimiento = fecha_nacimiento;
	}
	public Date getFecha_contrato() {
		return fecha_contrato;
	}
	public void setFecha_contrato(Date fecha_contrato) {
		this.fecha_contrato = fecha_contrato;
	}
	public String getNSS() {
		return NSS;
	}
	public void setNSS(String nSS) {
		NSS = nSS;
	}
	
	private String telefono;
  private Date   fecha_nacimiento;
  private Date   fecha_contrato;
  private String NSS;
  
  // Constructor
  public Trabajador (String nombre, String NSS)
  {
    this.nombre = nombre;
    this.NSS = NSS;
  }

  // Comparación de objetos
  public boolean equals (Trabajador t)
  {
    return this.NSS.equals(t.NSS);
  }
  
  // Conversión en una cadena de caracteres
  public String toString ()
  {
    return nombre + " (NSS "+NSS+")";
  }
  
//Paga por horas
 public double calcularPaga ()
 {
   return 0.0;
 }
}