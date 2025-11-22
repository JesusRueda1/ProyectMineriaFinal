{ pkgs, ... }:

{
  # 1. Paquetes del Sistema (Nix)
  # Solo instalamos Python y Pip aquí. Las librerías específicas van en requirements.txt
  packages = [
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.python3Packages.virtualenv
  ];

  # 2. Variables de Entorno
  env = {
    # Streamlit necesita saber qué puerto usar
    PORT = "9000"; 
  };

  # 3. Configuración del Espacio de Trabajo
  idx = {
    extensions = [
      "ms-python.python"
    ];

    workspace = {
      # Se ejecuta UNA vez al crear el entorno
      onCreate = {
        setup-venv = ''
          python3 -m venv .venv
          source .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '';
      };
      # Se ejecuta cada vez que reinicias la máquina
      onStart = {
        install-deps = ''
          source .venv/bin/activate
          pip install -r requirements.txt
        '';
      };
    };

    # 4. Vista Previa (El botón "Preview")
    previews = {
      enable = true;
      previews = {
        web = {
          # Usamos el streamlit DENTRO del entorno virtual (.venv)
          command = [
            "./.venv/bin/streamlit"
            "run"
            "main.py"
            "--server.port"
            "$PORT"
            "--server.address"
            "0.0.0.0"
            "--server.enableCORS"
            "false"
            "--server.enableXsrfProtection"
            "false"
          ];
          manager = "web";
        };
      };
    };
  };
}