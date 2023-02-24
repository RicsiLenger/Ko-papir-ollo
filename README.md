# Kő-Papír-Olló

## A játék lényege

Nevéből adódoan három szímbólum szerepel a játékban, a Kő, a Papír és az Olló. A játékot áltabán ketten játszák, egyszerre felmutatva a három szímbólumból egyet. A papír legyőzi a követ de az ollót nem, a kő legyőzi az ollót de a papírt nem és az olló legyőzi a papírt de a követ nem.

## A program indítása

A program indítása után egyből a játék panelnél találjuk magunkat. Itt tudunk választani a három opció közül amelyek a kő, a papír és az olló. A Leírás gombra kattintva tudjuk elolvasni a játékszabályokat. Ha kiválasztottuk a számunkra megfelelő szimbólumot, akkor a játék gombra kattintva gép is "kiválaszt" magának egy szimbólumot, így helyettesitve a második játékost. A program kiírja a számítógép által választott szímbólumot, majd megállapítja a nyertest. A program tarlamaz egy "Win Streak" funkciót,amely azt a célt szolgálja, hogy számolja a nyert köröket a Játékos által, ha a számítógép nyer, nullázódik.

## Függvények működése
> - *--init--():* Létrehozza a játék ablakát, a Radio gombokat, a Játék leírás gombot, és a játék gombot -> Erre kattintva belépünk a play_game():-be.
> - *play_game():* Megállapítja a játékot választását, majd generál a számítógépnek egy választ és eldöndti ki a nyertes.
> - *show_game_description():* messagebox-ban jeleníti meg a játékleírást.
