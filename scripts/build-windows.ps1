param(
    [string]$Python = (Join-Path $PSScriptRoot '../.venv/Scripts/python.exe')
)

$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT') {
    throw 'Run this script on Windows.'
}

$Python = (Get-Command $Python -ErrorAction Stop).Source
$originalPath = $env:PATH

Push-Location (Join-Path $PSScriptRoot '..')
try {
    & $Python -c "import platform, sys; sys.exit(0 if sys.version_info[:3] == (3, 12, 14) and platform.machine() == 'AMD64' else 'Python 3.12.14 (Windows x64) is required')"
    if ($LASTEXITCODE -ne 0) { throw 'Unsupported Python version or architecture.' }
    & $Python -m pip install -r requirements-windows.txt
    if ($LASTEXITCODE -ne 0) { throw 'Dependency installation failed.' }
    & $Python -m pip check
    if ($LASTEXITCODE -ne 0) { throw 'Dependency validation failed.' }
    # Keep unrelated tools' DLLs (for example Poppler's ICU) out of the bundle.
    $env:PATH = "$(Split-Path $Python);$env:SystemRoot\System32;$env:SystemRoot"
    & $Python -m PyInstaller --noconfirm --clean --windowed --onedir --name HealthCareAPP main.py
    if ($LASTEXITCODE -ne 0) { throw 'Windows build failed.' }
    Write-Output 'Distribution: dist/HealthCareAPP (copy the entire folder).'
}
finally {
    $env:PATH = $originalPath
    Pop-Location
}
