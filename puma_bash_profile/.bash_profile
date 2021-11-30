# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

export MKLROOT=/nfs/home/zyt329/intel/oneapi/mkl/latest/

ulimit -s unlimited

export PATH="$HOME/intel/oneapi/compiler/latest/linux/bin/intel64:$PATH"
