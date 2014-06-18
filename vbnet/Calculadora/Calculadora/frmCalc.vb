Public Class frmCalc
    Dim numero1 As Double
    Dim numero2 As Double
    Dim contador As Boolean
    Dim tipo As String


    Private Sub b1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b1.Click
        txtCal.AppendText(b1.Text)
        If contador = True Then
            txtCal2.AppendText(b1.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b2.Click
        txtCal.AppendText(b2.Text)
        If contador = True Then
            txtCal2.AppendText(b2.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b0_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b0.Click
        txtCal.AppendText(b0.Text)
        If contador = True Then
            txtCal2.AppendText(b0.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b3.Click
        txtCal.AppendText(b3.Text)
        If contador = True Then
            txtCal2.AppendText(b3.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b4.Click
        txtCal.AppendText(b4.Text)
        If contador = True Then
            txtCal2.AppendText(b4.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b5.Click
        txtCal.AppendText(b5.Text)
        If contador = True Then
            txtCal2.AppendText(b5.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b6_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b6.Click
        txtCal.AppendText(b6.Text)
        If contador = True Then
            txtCal2.AppendText(b6.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b7_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b7.Click
        txtCal.AppendText(b7.Text)
        If contador = True Then
            txtCal2.AppendText(b7.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b8_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b8.Click
        txtCal.AppendText(b8.Text)
        If contador = True Then
            txtCal2.AppendText(b8.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub b9_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles b9.Click
        txtCal.AppendText(b9.Text)
        If contador = True Then
            txtCal2.AppendText(b9.Text)
            numero2 = txtCal2.Text
        End If
    End Sub

    Private Sub bSum_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles bSum.Click
        numero1 = txtCal.Text
        txtCal.AppendText(bSum.Text)
        contador = True
        tipo = "+"
    End Sub

    Private Sub bCalcular_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles bCalcular.Click
        If tipo = "+" Then
            txtCal.Text = numero1 + numero2
        ElseIf tipo = "-" Then
            txtCal.Text = numero1 - numero2
        ElseIf tipo = "*" Then
            txtCal.Text = numero1 * numero2
        ElseIf tipo = "/" Then
            txtCal.Text = numero1 / numero2
        Else
            Exit Sub
        End If

        numero1 = 0
        numero2 = 0
        contador = False
        txtCal2.Text = ""
        tipo = ""

    End Sub

    Private Sub bRest_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles bRest.Click
        numero1 = txtCal.Text
        txtCal.AppendText(bRest.Text)
        contador = True
        tipo = "-"
    End Sub

    Private Sub bMult_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles bMult.Click
        numero1 = txtCal.Text
        txtCal.AppendText(bMult.Text)
        contador = True
        tipo = "*"
    End Sub

    Private Sub bDiv_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles bDiv.Click
        numero1 = txtCal.Text
        txtCal.AppendText(bDiv.Text)
        contador = True
        tipo = "/"
    End Sub

    Private Sub frmCalc_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        txtCal2.Visible = False
    End Sub

    Private Sub bClear_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles bClear.Click
        numero1 = 0
        numero2 = 0
        contador = False
        txtCal.Text = ""
        txtCal2.Text = ""
        tipo = ""
    End Sub

    Private Sub bComa_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles bComa.Click
        txtCal.AppendText(bComa.Text)
        If contador = True Then
            txtCal2.AppendText(bComa.Text)
            numero2 = txtCal2.Text
        End If
    End Sub
End Class
