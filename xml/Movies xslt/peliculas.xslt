<?xml version="1.0" encoding="utf-8" ?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" >

<!-- tipo de salida -->
<xsl:output method="html" />

<!-- template principal -->
<xsl:template match="/">
	<html>
	<head><title>Películas</title>
	<link rel="stylesheet" href="style.css" />
	</head>
	<body>
		<h1>Listado de Películas</h1>
	<table>
	
		<tr>
			<th>Película</th>
			<th>Acerca</th>
		</tr>
	<xsl:for-each select="/movieDB/movie"> 
		<tr>
			<td>
				<img><xsl:attribute name="src"><xsl:value-of select="concat('pictures/', ./still)"/></xsl:attribute></img>
				
			</td>
			<td>
				<p>Título: <xsl:value-of select="title" /><br/>
				Productora: <xsl:value-of select="producer"/><br/>
				Director: <xsl:value-of select="concat(./director/forename, ' ', ./director/surname)"/><br/>
				Año: <xsl:value-of select="year"/></p>
			</td>
		</tr>
	</xsl:for-each>
	</table>
	<br/><br/><br/>
	<h1>Listado de Actores</h1>
	<table>
	
		<tr>
			<th>Actor</th>
			<th>Acerca</th>
		</tr>
		<xsl:for-each select="/movieDB/movie/actor"> 
		<tr>
			<td>
				<img><xsl:attribute name="src"><xsl:value-of select="concat('pictures/', ./picture)"/></xsl:attribute></img>
			</td>
			<td>
				<p>Nombre: <xsl:value-of select="forename" />
				<br/>
				Apellido: <xsl:value-of select="surname" />
				<br/>
				Sexo: <xsl:value-of select="sex" /><br/>
				F. Nacimiento: <xsl:value-of select="birthdate" />
				</p>
			</td>
		</tr>
	</xsl:for-each>
	</table>

	</body>
	</html>
</xsl:template>

</xsl:stylesheet>
