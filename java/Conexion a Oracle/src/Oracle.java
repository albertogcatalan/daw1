import java.sql.*;

public class Oracle {
	
		
	public ResultSet ejecutarconsulta (String consulta) throws ClassNotFoundException, SQLException{
		// 1. Cargar el driver
		Class.forName ("oracle.jdbc.OracleDriver");
		// 2. Conectar con la base de datos
						
		Connection conn = DriverManager.getConnection
						("jdbc:oracle:thin:@172.30.160.190:1521/enlaces6","daw20", "tiger");
						
		Statement st = conn.createStatement();
		ResultSet rs = st.executeQuery(consulta);
		
		return rs;
	}
	
	
	
	
	
	
	
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// 1. Cargar el driver
		Class.forName ("oracle.jdbc.OracleDriver");
		// 2. Conectar con la base de datos
		
		Connection conn = DriverManager.getConnection
		     ("jdbc:oracle:thin:@172.30.160.190:1521/enlaces6",
		    		 "daw20", "tiger");
		
		Statement st = conn.createStatement();
		String sql = "select * from emp";
		
		ResultSet rs = st.executeQuery(sql);
		
		// obtener metadatos:
		ResultSetMetaData metaData = rs.getMetaData();

		int cols = metaData.getColumnCount();

		System.out.println("Nombre de la tabla : " + 
					metaData.getTableName(2));
		System.out.println("Campo \ttamaño\tTipo");

		for (int i = 0; i < cols; i++) {
			System.out.print(metaData.getColumnName(i + 1) + " \t");
			System.out.print(metaData.getColumnDisplaySize(i + 1) + "\t");
			System.out.println(metaData.getColumnTypeName(i + 1));
			}
		// TODO: escribir nombres de columnas
		System.out.println("Nombre em.\tPuesto de trabajo");
		while(rs.next()){
			System.out.println(rs.getNString(2) + "\t" +
					rs.getNString(3).toLowerCase());
		}
		
		rs.close();
		
		conn.close();
	}
}