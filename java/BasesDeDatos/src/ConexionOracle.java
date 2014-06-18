import java.sql.*;

public class ConexionOracle {

	/**
	 * @param args
	 * @throws ClassNotFoundException 
	 * @throws SQLException 
	 */
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// cargar el driver
		Class.forName("oracle.jdbc.driver.OracleDriver");
		
		// conectar con la base de datos
		String cadena_con = "jdbc:oracle:thin:@172.30.160.190:1521/enlaces6";
		Connection conn = DriverManager.getConnection(cadena_con, "daw20", "tiger");
		
		Statement sentencia = conn.createStatement();
		String sql = "select * from emp";
		ResultSet rs = sentencia.executeQuery(sql);
		
		ResultSetMetaData metaData = rs.getMetaData();
		
		int cols = metaData.getColumnCount();
		
		System.out.println("Nombre de la tabla: "+ metaData.getTableName(2));
		System.out.println("Campo \tTama–o\tTipo");
		
		for (int i=0;i< cols;i++){
			System.out.print(metaData.getColumnName(i + 1) + " \t");
			System.out.print(metaData.getColumnDisplaySize(i + 1) + " \t");
			System.out.println(metaData.getColumnTypeName(i + 1) + " \t");
			
		}
		
		// mostrar nombres
		System.out.println("Nombre em.\tPuesto de trabajo");
		while(rs.next()){
			System.out.println(rs.getNString(2)+"\t"+rs.getNString(3));
		}
		
		
		
		
		// cierre de la conexi—n
		rs.close();
	    conn.close();
		

	}

}
