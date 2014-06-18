<?xml version="1.0" encoding="UTF-8" ?>
<!--
    peliculas
-->

<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output encoding="UTF-8" indent="yes" method="html" />

    <xsl:template match="/">
    	<html>
    	<head><title>Películas</title></head>
    	<body>
    		<h1>Mis peliculas</h1>
    		<p>Mi favorita es:
	    		<strong><xsl:value-of select="/movies/movie[1]/title"/>
	    		</strong>
	    		<h2>Listado de peliculas</h2>
	    		<table border="1" width="75%">
	    		<tr>
	    			<th>Título</th>
	    			<th>Productor</th>
	    			<th>Tipo</th>
	    			<th>Año</th>
	    		</tr>
	    		
	    		<xsl:for-each select="/movies/movie/title">
	    		<xsl:sort select="../@year" order="ascending"/>
	    		<tr>
	    			<td><xsl:value-of select="."/></td>
	    			<td><xsl:value-of select="../producer"/></td>
	    			<td><xsl:value-of select="../@type"/></td>
	    			<td><xsl:value-of select="../@year"/></td>
	    		</tr>
	    		
	    		</xsl:for-each>
	    		</table>
    		</p>
    	</body>
    	</html>
    </xsl:template>
</xsl:stylesheet>