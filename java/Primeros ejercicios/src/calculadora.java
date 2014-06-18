import javax.swing.*;

public class calculadora {

	public static void main (String [] args) {
		Double val1, val2;
		
	    String valor1 = JOptionPane.showInputDialog("Introduce un numero");
	    String operador1 = JOptionPane.showInputDialog("Introduce un operador");
	    String valor2 = JOptionPane.showInputDialog("Introduce un numero");
	    
	    val1 = new Double(valor1);
	    val2 = new Double(valor2);
	    
	    switch (operador1.charAt(0)){
	    	case '+': JOptionPane.showMessageDialog(null,"Resultado: " + (val1 + val2)); break;
	    	case '-': JOptionPane.showMessageDialog(null,"Resultado: " + (val1 - val2)); break;
	    	case '*': JOptionPane.showMessageDialog(null,"Resultado: " + (val1 * val2)); break;
	    	case '/': JOptionPane.showMessageDialog(null,"Resultado: " + (val1 / val2)); break;
	    	default: JOptionPane.showMessageDialog(null,"No has insertado operador");
	    }
	 
	    
	  }

}
