{
  outputs = {nixpkgs, ... }: {
    devShells.x86_64-linux.default = let
      pkgs = import nixpkgs {
        system = "x86_64-linux";
	config.allowUnfree = true;
      };
    in 
      pkgs.mkShell {
        name = "Post-It";
        packages = with pkgs; [
          python310
	        python310Packages.tweepy
	        python310Packages.flask
	        pkgs.python310Packages.tkinter
	        python310Packages.flask-restful
	        python310Packages.requests-oauthlib
          python310Packages.colorama
        ];
      };
  };
}
