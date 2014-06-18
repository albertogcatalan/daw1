
public class Producto {
	
	private Integer prodid;
	private String descripcion;
	private Float precionormal;
	private Float preciominimo;
	private Integer existencias;
	private Float tipoiva;
	
	
	public Producto()
	{}
	
	public Producto(Integer prodid, String descripcion, Float precionormal,
			Float preciominimo, Integer existencias, Float tipoiva) {
		this.prodid = prodid;
		this.descripcion = descripcion;
		this.precionormal = precionormal;
		this.preciominimo = preciominimo;
		this.existencias = existencias;
		this.tipoiva = tipoiva;
	}
	public Integer getProdid() {
		return prodid;
	}
	public void setProdid(Integer prodid) {
		this.prodid = prodid;
	}
	public String getDescripcion() {
		return descripcion;
	}
	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}
	public Float getPrecionormal() {
		return precionormal;
	}
	public void setPrecionormal(Float precionormal) {
		this.precionormal = precionormal;
	}
	public Float getPreciominimo() {
		return preciominimo;
	}
	public void setPreciominimo(Float preciominimo) {
		this.preciominimo = preciominimo;
	}
	public Integer getExistencias() {
		return existencias;
	}
	public void setExistencias(Integer existencias) {
		this.existencias = existencias;
	}
	public Float getTipoiva() {
		return tipoiva;
	}
	public void setTipoiva(Float tipoiva) {
		this.tipoiva = tipoiva;
	}
	
	

}
