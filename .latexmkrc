$pdf_mode = 4;  # Use lualatex
$lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -shell-escape %O %S';
$out_dir = '../build';
$bibtex_use = 2;

# Pre-create output subdirectories to mirror the src/ tree.
# latexmk with -outdir cannot create deeply nested directories on its own
# (e.g., build/part2_black_holes/ch04_schwarzschild/), which breaks CI and
# fresh clones.  We scan src/ for subdirectories and replicate the structure
# under build/.
#
# Note: .latexmkrc is evaluated from the project root (before -cd takes
# effect), so paths are relative to the project root, not src/.
use File::Find;
use File::Path qw(make_path);
my @src_dirs;
find(sub { push @src_dirs, $File::Find::name if -d }, 'src');
for my $d (@src_dirs) {
    (my $rel = $d) =~ s|^src/||;
    next if $rel eq 'src';
    make_path("build/$rel");
}
