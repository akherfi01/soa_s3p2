function Change-DirectoryAndRun {
    # Hard-coded directory path and command
    $DirectoryPath = "C:\Users\sam20\Documents\soa\soa_s3p2\project\frontend"
    $Command = "npm"
    $Arguments = "run dev"

    # Check if npm is installed and available
    if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
        Write-Host "npm is not recognized. Please ensure npm is installed and available in the PATH."
        return
    }

    # Run npm in the specified directory and wait for it to finish
    Start-Process -FilePath $Command -ArgumentList $Arguments -WorkingDirectory $DirectoryPath -Wait -NoNewWindow

    # Optionally, provide feedback about the status of the command
    Write-Host "npm run dev command has finished executing."
}
