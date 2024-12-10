$totalSteps = 3
$currentStep = 0

function Update-Progress {
    param (
        [string]$Activity,
        [int]$PercentComplete
    )
    Write-Progress -Activity $Activity -PercentComplete $PercentComplete
}

$currentStep++
$percentComplete = ($currentStep / $totalSteps) * 100
Update-Progress -Activity "Creating virtual environment..." -PercentComplete $percentComplete

Write-Host "Creating virtual environment..."
python -m venv .env
if ($?) {
    Write-Host "Virtual environment created successfully."
} else {
    Write-Error "Failed to create virtual environment."
    exit 1
}

$currentStep++
$percentComplete = ($currentStep / $totalSteps) * 100
Update-Progress -Activity "Activating virtual environment..." -PercentComplete $percentComplete

Write-Host "Activating virtual environment..."
& .\.env\Scripts\Activate.ps1
if ($?) {
    Write-Host "Virtual environment activated successfully."
} else {
    Write-Error "Failed to activate virtual environment."
    exit 1
}

$currentStep++
$percentComplete = ($currentStep / $totalSteps) * 100
Update-Progress -Activity "Installing required packages..." -PercentComplete $percentComplete

Write-Host "Installing required packages..."
pip install -r requirements.txt
if ($?) {
    Write-Host "Required packages installed successfully."
} else {
    Write-Error "Failed to install required packages."
    exit 1
}

Update-Progress -Activity "Completed!" -PercentComplete 100
Write-Host "All steps completed successfully!"
