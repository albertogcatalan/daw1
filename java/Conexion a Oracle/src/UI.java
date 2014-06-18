import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumn;

import java.sql.*;

public class UI extends JFrame{
	
	JTextField textConsulta;
	JButton botonEj,botonClear;
	JTable tablaResult;
	Oracle conn = new Oracle();
	JScrollPane scrollPanel;
	JPanel panel;
	
	
	public UI() {
		super();
		setSize(600, 300);
		setTitle("Ejecutar consultas Oracle");
		setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		setResizable(false);
		panel = (JPanel) this.getContentPane();
		panel.setLayout(new GridLayout(3,1));
		
		textConsulta = new JTextField(100);
		panel.add(textConsulta);
		
		botonEj = new JButton("Ejecutar");
		escuchar(botonEj);		
		botonClear = new JButton("Limpiar");
		escuchar(botonClear);
		
		JPanel panelc = new JPanel();
		panelc.setLayout(new GridLayout(1, 2));
		panelc.add(botonEj);
		panelc.add(botonClear);
		panel.add(panelc);
		
		tablaResult = new JTable();
		panel.add(tablaResult);
		
		scrollPanel= new JScrollPane();
		scrollPanel.add(tablaResult);
		
		panel.add(scrollPanel);
	}
	
	public void escuchar (JButton accion){
		accion.addMouseListener(new MouseAdapter() {
			public void mouseReleased(MouseEvent evt){
				JButton btn = (JButton) evt.getSource();
				try {
					operacion(btn.getText());
				} catch (ClassNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}				
			}
		});
	}
	
	public void operacion (String accion) throws ClassNotFoundException, SQLException{
		if (accion == "Ejecutar"){

			// ejecutamos la consulta del textfield
			ResultSet rs = conn.ejecutarconsulta(textConsulta.getText());
			
			// obtener metadatos
			ResultSetMetaData metaData = rs.getMetaData();

			int cols = metaData.getColumnCount();
			//Guardamos los nombres de las columnas en un array
            String[] columnNames = new String[cols];
            for (int i = 0; i < cols; i++) {
                    columnNames[i] = metaData.getColumnName(i + 1);
                    }
            
            //Creamos un table model, que es lo que modificaremos para pegarlo en la tabla
            DefaultTableModel tablaModel = new DefaultTableModel(null,columnNames);
            
            //Extraemos los datos de la consulta por filas y los añadimos al table model
            String[] datos = new String[cols]; 
            //Pasamos los datos de rs al array que nos hemos creado
			while(rs.next()){
				for (int i = 0; i < cols; i++){
					if (rs.getNString(i+1)== null){
						datos[i] = " ";
					}
					else{
						datos[i] = rs.getNString(i+1);
					}
				
				}
				tablaModel.addRow(datos); //introducimos los datos al table model
			}
			
			tablaResult.setModel(tablaModel); //Metemos el tableModel en la tabla
            scrollPanel.add(tablaResult); //Metemos la tabla en el scrolPanel
            
            scrollPanel.setViewportView(tablaResult); //Actualizamos el scrollPanel
			
		}
		else {
			textConsulta.setText("");
		}
			
		
	}
	
	

}
