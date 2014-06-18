
public class LineaPedido {
	private Integer numerolineapedido;
	private Producto producto;
	private Float precioactual;
	private Integer unidades;
	private Float descuento;
	private Float totallinea;
	public Integer getNumerolineapedido() {
		return numerolineapedido;
	}
	public void setNumerolineapedido(Integer numerolineapedido) {
		this.numerolineapedido = numerolineapedido;
	}
	public Producto getProducto() {
		return producto;
	}
	public void setProducto(Producto producto) {
		this.producto = producto;
	}
	public Float getPrecioactual() {
		return precioactual;
	}
	public void setPrecioactual(Float precioactual) {
		this.precioactual = precioactual;
	}
	public Integer getUnidades() {
		return unidades;
	}
	public void setUnidades(Integer unidades) {
		this.unidades = unidades;
	}
	public Float getDescuento() {
		return descuento;
	}
	public void setDescuento(Float descuento) {
		this.descuento = descuento;
	}
	public Float getTotallinea() {
		return totallinea;
	}
	public void setTotallinea(Float totallinea) {
		this.totallinea = totallinea;
	}
	
	
}
