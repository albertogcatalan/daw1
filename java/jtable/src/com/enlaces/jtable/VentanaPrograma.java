package com.enlaces.jtable;

import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.WindowConstants;

public class VentanaPrograma extends JFrame {
		JTextField pantalla;

		/** guarda el resultado de la operacion anterior o el nœmero tecleado */
		double resultado;

		/** para guardar la operacion a realizar */
		String operacion;

		/** Los paneles donde colocaremos los botones */
		JPanel panelPrincipal, panelBotones;

		/** Indica si estamos iniciando o no una operaci—n */
		boolean nuevaOperacion = true;

		/**
		 * Constructor. Crea los botones y componentes
		 */
		public VentanaPrograma() {
			super();
			setSize(300, 300);
			setTitle("Conversor Temperatura");
			setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
			setResizable(false);

			// panel principal
			JPanel panel = (JPanel) this.getContentPane();
			panel.setLayout(new GridLayout(4, 1));
			
			// label de titulo
			JLabel labelTitle = new JLabel("Conversor Temp.");
			labelTitle.setFont(new Font("Arial", Font.BOLD, 25));
			labelTitle.setHorizontalAlignment(JLabel.CENTER);
			panel.add("North", labelTitle);
			
			// caja de texto superior
			pantalla = new JTextField("0");
			pantalla.setHorizontalAlignment(JTextField.RIGHT);
			pantalla.setEditable(true);
			panel.add("North", pantalla);
			
			// caja de texto inferior
			pantalla = new JTextField("0");
			pantalla.setHorizontalAlignment(JTextField.RIGHT);
			pantalla.setEditable(false);
			panel.add("North", pantalla);
		
			// panel botones de accion
			panelBotones = new JPanel();
			panelBotones.setLayout(new GridLayout(1, 2));

			nuevoBotonOperacion("Convertir");
			nuevoBotonOperacion("Reiniciar");

			panel.add("South", panelBotones);

			validate();
		}

		/**
		 * Boton de accion del programa
		 */
		private void nuevoBotonOperacion(String operacion) {
			JButton btn = new JButton(operacion);
			btn.setForeground(Color.RED);

			btn.addMouseListener(new MouseAdapter() {

				@Override
				public void mouseReleased(MouseEvent evt) {
					JButton btn = (JButton) evt.getSource();
					operacionPulsado(btn.getText());
				}
			});

			panelBotones.add(btn);
		}

		/**
		 * Gestiona el gestiona las pulsaciones de teclas de operaci—n
		 * 
		 */
		private void operacionPulsado(String tecla) {
			if (tecla.equals("Convertir")) {
				calcularResultado();
			} else {
				resultado = 0;
				pantalla.setText("0");
				nuevaOperacion = true;
			}

			nuevaOperacion = true;
		}

		/**
		 * Calcula el resultado y lo muestra por pantalla
		 */
		private void calcularResultado() {
			
			if (operacion.equals("+")) {
				resultado += new Double(pantalla.getText());
			} else if (operacion.equals("-")) {
				resultado -= new Double(pantalla.getText());
			} else if (operacion.equals("/")) {
				resultado /= new Double(pantalla.getText());
			} else if (operacion.equals("*")) {
				resultado *= new Double(pantalla.getText());
			}

			pantalla.setText("" + resultado);
			operacion = "";
		}
		
	}
