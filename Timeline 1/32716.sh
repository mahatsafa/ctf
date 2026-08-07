for i in {32710..32725}; do
    echo "===== $i ====="
    icat partition4.img $i 2>/dev/null | head
done
