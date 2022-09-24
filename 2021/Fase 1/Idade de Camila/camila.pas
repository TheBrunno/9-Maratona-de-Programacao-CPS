program camila;
var 
    idades: array[0..2] of integer;
    idade, i, idade_camila: integer;
begin
    i := 0;
    while(i < 3) do
    begin
        read(idade);
        if (idade > 5) and (idade < 100) then
        begin
            idades[i] := idade;
            i := i+1;
            if ((idades[0] > idades[1]) and (idades[0] < idades[2]) or (idades[0] < idades[1]) and (idades[0] > idades[2])) then
            begin
                idade_camila := idades[0];
            end
            else if ((idades[1] > idades[0]) and (idades[1] < idades[2]) or (idades[1] < idades[0]) and (idades[1] > idades[2])) then
            begin
                idade_camila := idades[1];
            end
            else if ((idades[2] > idades[1]) and (idades[2] < idades[0]) or (idades[2] < idades[1]) and (idades[2] > idades[0])) then
            begin
                idade_camila := idades[2];
            end
            else
            begin
                idade_camila := idades[0];
            end;
        end;
    end;
    writeln(idade_camila)
end.