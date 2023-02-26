Sub GetResults()
    Dim ws As Worksheet

    For Each ws In Worksheets
        Call WriteTickerSummaryTitles(ws)
        Call WriteGreatestSummaryTitles(ws)
        
        Call GetTickerSummary(ws)
    Next
End Sub
Sub GetTickerSummary(ws As Worksheet)
    Dim TickerSymbol As String
    
    Dim OpeningPrice As Double
    Dim ClosingPrice As Double
    Dim YearlyChange As Double
    Dim PercentChange As Double
    Dim TotalStockVolume As Double
    
    Dim GreatestPercentIncrease As Double
    Dim GreatestPercentDecrease As Double
    Dim GreatestTotalVolume As Double
    
    Dim GreatestPercentIncreaseTicker As String
    Dim GreatestPercentDecreaseTicker As String
    Dim GreatestTotalVolumeTicker As String
    
    Dim ResultPosition As Integer
    ResultPosition = 2
    
    Dim DataRange As Range
    Set DataRange = ws.Range("A2", ws.Range("G2").End(xlDown))
    
    DataRange.Sort Key1:=DataRange.Range("A1"), _
                    Order1:=xlAscending, _
                    Header:=xlYes, _
                    Key2:=DataRange.Range("B1"), _
                    Order2:=xlAscending, _
                    Header:=xlYes

    For Each currentRow In DataRange.Rows
        
        If TickerSymbol <> currentRow.Cells(1, 1).Value Then
        
            If TickerSymbol <> "" Then
                YearlyChange = ClosingPrice - OpeningPrice
                PercentChange = (YearlyChange) / OpeningPrice
                
                If PercentChange >= 0 And PercentChange > GreatestPercentIncrease Then
                    GreatestPercentIncrease = PercentChange
                    GreatestPercentIncreaseTicker = TickerSymbol
                ElseIf PercentChange < 0 And PercentChange < GreatestPercentDecrease Then
                    GreatestPercentDecrease = PercentChange
                    GreatestPercentDecreaseTicker = TickerSymbol
                End If
                
                If TotalStockVolume > GreatestTotalVolume Then
                    GreatestTotalVolume = TotalStockVolume
                    GreatestTotalVolumeTicker = TickerSymbol
                End If
            
                Call WriteTickerSummaryResult(TickerSymbol, YearlyChange, PercentChange, TotalStockVolume, ResultPosition, ws)
                
                ResultPosition = ResultPosition + 1
            End If
        
            TickerSymbol = currentRow.Cells(1, 1).Value
            
            If TickerSymbol = "" Then
                Exit For
            End If
            
            OpeningPrice = currentRow.Cells(1, 3).Value
            ClosingPrice = currentRow.Cells(1, 6).Value
            
            TotalStockVolume = currentRow.Cells(1, 7).Value
        Else
            ClosingPrice = currentRow.Cells(1, 6).Value
            TotalStockVolume = TotalStockVolume + currentRow.Cells(1, 7).Value
        End If
    Next
    
    Call WriteGreatestSummaryResult(GreatestPercentIncreaseTicker, GreatestPercentIncrease, _
            GreatestPercentDecreaseTicker, GreatestPercentDecrease, GreatestTotalVolumeTicker, GreatestTotalVolume, ws)
    
End Sub
Sub WriteTickerSummaryTitles(ws As Worksheet)
    ws.Range("I1").Value = "Ticker Symbol"
    ws.Range("J1").Value = "Yearly Change"
    ws.Range("K1").Value = "PercentChange"
    ws.Range("L1").Value = "Total Volume"
End Sub
Sub WriteGreatestSummaryTitles(ws As Worksheet)
    ws.Range("O2").Value = "Greatest % Increase"
    ws.Range("O3").Value = "Greatest % Decrease"
    ws.Range("O4").Value = "Greatest Total Volume"
    
    ws.Range("P4").Value = "Ticker"
    ws.Range("Q4").Value = "Value"
End Sub
Sub WriteTickerSummaryResult(TickerSymbol As String, YearlyChange As Double, PercentChange As Double, TotalVolume As Double, Position As Integer, ws As Worksheet)
    ws.Cells(Position, 9).Value = TickerSymbol
    ws.Cells(Position, 10).Value = Format(YearlyChange, "0.00")
    ws.Cells(Position, 11).Value = Format(PercentChange, "0.00%")
    ws.Cells(Position, 12).Value = TotalVolume
    
    If YearlyChange < 0 Then
        ws.Cells(Position, 10).Interior.ColorIndex = 3
    Else
        ws.Cells(Position, 10).Interior.ColorIndex = 4
    End If
End Sub
Sub WriteGreatestSummaryResult(GreatestPercentIncreaseTicker As String, GreatestPercentIncrease As Double, _
                                GreatestPercentDecreaseTicker As String, GreatestPercentDecrease As Double, _
                                 GreatestTotalVolumeTicker As String, GreatestTotalVolume As Double _
                                 , ws As Worksheet)
    ws.Range("P2").Value = GreatestPercentIncreaseTicker
    ws.Range("Q2").Value = Format(GreatestPercentIncrease, "0.00%")
    
    ws.Range("P3").Value = GreatestPercentDecreaseTicker
    ws.Range("Q3").Value = Format(GreatestPercentDecrease, "0.00%")
    
    ws.Range("P4").Value = GreatestTotalVolumeTicker
    ws.Range("Q4").Value = GreatestTotalVolume
End Sub









