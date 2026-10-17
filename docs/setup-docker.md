# Complete the local Docker prerequisite

Inspection on 17 October 2026 found no Docker executable, engine pipe or Docker Desktop installation. `wsl --status` reports that Windows Subsystem for Linux is not installed. Hosted CI already builds and smoke-tests the container, but the exam also describes local build/run evidence.

## Windows steps for the computer owner

Save all work first. Complete these steps yourself because Windows may require administrator authorization and a restart. Do not restart while unsaved work is open.

1. Open PowerShell as Administrator and run:

```powershell
wsl --install
```

2. Follow Microsoft's prompts and restart only when requested. Finish any Linux first-run setup directly; do not share its password in chat. Verify:

```powershell
wsl --version
wsl --status
```

3. Download Docker Desktop from its [official Windows installation page](https://docs.docker.com/desktop/setup/install/windows-install/). Use the installer appropriate to your processor. Follow the supported Windows and hardware requirements on that page.
4. Choose the WSL 2 backend and the per-user installation where offered. Read and personally accept Docker's agreement if you agree. Start Docker Desktop and wait until the engine is running. Do not change BIOS settings or other system settings without understanding the displayed prerequisite.
5. Open a new PowerShell window and confirm both client and server are reported:

```powershell
docker version
```

## Build and verify the actual exam project

From the shared-exam-project directory:

```powershell
docker build -t sample-api:local .
docker run --rm -p 8000:8000 sample-api:local
```

In a second PowerShell window:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

The real result should contain `status` equal to `ok`. Capture the build output, running container and health response. Stop the foreground container with Ctrl+C when finished. Only mark issue #4 complete after this actual execution succeeds. No local Docker success is claimed yet.

Microsoft source: https://learn.microsoft.com/en-us/windows/wsl/install

Docker source: https://docs.docker.com/desktop/setup/install/windows-install/
