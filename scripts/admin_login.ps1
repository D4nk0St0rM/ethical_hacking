$username="admin"
$password="p@ssw0rd"
$url_login="127.0.0.1/login.php"

$ie = New-Object -com InternetExplorer.Application
$ie.Visible = $false
$ie.navigate("$url_login")
while($ie.ReadyState -ne 4){ start-sleep -m 1000}
$ie.document.getElementsByName("username")[0].value="$username"
$ie.document.getElementsByName("password")[0].value="$password"
start-sleep -m 10
$ie.document.getElementsByClassName("btn")[0].click()
start-sleep -m 100
$ie.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ie)