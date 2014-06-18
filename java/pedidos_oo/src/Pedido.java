import java.util.ArrayList;
import java.util.GregorianCalendar;


public class Pedido {
	private Integer numeropedido;
	private GregorianCalendar fechapedido;
	private Cliente cliente;
	private ArrayList <LineaPedido> lineaspedido;
	private Float baseimponible;
	private Float impuestos;
	private Float totaldescuentos;
	private Float total;
	public Integer getNumeropedido() {
		return numeropedido;
	}
	public void setNumeropedido(Integer numeropedido) {
		this.numeropedido = numeropedido;
	}
	public GregorianCalendar getFechapedido() {
		return fechapedido;
	}
	public void setFechapedido(GregorianCalendar fechapedido) {
		this.fechapedido = fechapedido;
	}
	public Cliente getCliente() {
		return cliente;
	}
	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}
	public ArrayList<LineaPedido> getLineaspedido() {
		return lineaspedido;
	}
	public void setLineaspedido(ArrayList<LineaPedido> lineaspedido) {
		this.lineaspedido = lineaspedido;
	}
	
	public Float getBaseimponible() {
		return baseimponible;
	}
	public void setBaseimponible(Float baseimponible) {
		this.baseimponible = baseimponible;
	}
	public Float getImpuestos() {
		return impuestos;
	}
	public void setImpuestos(Float impuestos) {
		this.impuestos = impuestos;
	}
	public Float getTotaldescuentos() {
		return totaldescuentos;
	}
	public void setTotaldescuentos(Float totaldescuentos) {
		this.totaldescuentos = totaldescuentos;
	}
	public Float getTotal() {
		return total;
	}
	public void setTotal(Float total) {
		this.total = total;
	}
	
	
	
	

}
