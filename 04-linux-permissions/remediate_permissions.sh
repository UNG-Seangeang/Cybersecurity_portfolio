#!/usr/bin/env bash
# ==============================================================================
# Script Name : remediate_permissions.sh
# Description : Automated Linux File Permissions Audit & Remediation Script
#               Enforces least-privilege access policies on the research team's
#               project directory (/home/researcher2/projects or local demo).
# Usage       : ./remediate_permissions.sh [--setup-demo] [target_directory]
# ==============================================================================

set -euo pipefail

# Formatting colors for terminal output
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
BLUE="\033[0;34m"
NC="\033[0m" # No Color

TARGET_DIR="${1:-./projects}"

# ------------------------------------------------------------------------------
# Helper: Setup a local mock lab environment for portfolio demonstration
# ------------------------------------------------------------------------------
setup_demo_env() {
    local demo_dir="./projects"
    echo -e "${BLUE}[*] Setting up mock lab environment in '${demo_dir}'...${NC}"
    mkdir -p "${demo_dir}/drafts"

    # Create sample files
    echo "Research Project K Data" > "${demo_dir}/project_k.txt"
    echo "Research Project M Data" > "${demo_dir}/project_m.txt"
    echo "Research Project R Data" > "${demo_dir}/project_r.txt"
    echo "Research Project T Data" > "${demo_dir}/project_t.txt"
    echo "Archived Project X Data" > "${demo_dir}/.project_x.txt"

    # Apply initial vulnerable permissions from the scenario
    chmod 666 "${demo_dir}/project_k.txt"   # -rw-rw-rw- (World-writable!)
    chmod 640 "${demo_dir}/project_m.txt"   # -rw-r----- (Compliant)
    chmod 664 "${demo_dir}/project_r.txt"   # -rw-rw-r-- (Compliant)
    chmod 664 "${demo_dir}/project_t.txt"   # -rw-rw-r-- (Compliant)
    chmod 620 "${demo_dir}/.project_x.txt"  # -rw--w---- (Archived file writable!)
    chmod 710 "${demo_dir}/drafts"          # drwx--x--- (Group can enter directory!)

    echo -e "${GREEN}[+] Mock environment created with initial unhardened permissions.${NC}\n"
}

# ------------------------------------------------------------------------------
# Helper: Check and remediate a specific target item
# ------------------------------------------------------------------------------
remediate_item() {
    local item_path="$1"
    local expected_symbolic="$2"
    local chmod_cmd="$3"
    local policy_desc="$4"

    if [[ ! -e "${item_path}" ]]; then
        echo -e "${RED}[!] Missing item: ${item_path}${NC}"
        return
    fi

    local current_symbolic
    current_symbolic=$(stat -c "%A" "${item_path}")
    local current_octal
    current_octal=$(stat -c "%a" "${item_path}")

    echo -e "${BLUE}Checking:${NC} ${item_path}"
    echo -e "  Policy          : ${policy_desc}"
    echo -e "  Current State   : ${current_symbolic} (${current_octal})"

    if [[ "${current_symbolic}" != "${expected_symbolic}" ]]; then
        echo -e "  Status          : ${YELLOW}NON-COMPLIANT${NC} -> Applying 'chmod ${chmod_cmd}'"
        chmod "${chmod_cmd}" "${item_path}"
        local new_symbolic
        new_symbolic=$(stat -c "%A" "${item_path}")
        local new_octal
        new_octal=$(stat -c "%a" "${item_path}")
        echo -e "  Remediated State: ${GREEN}${new_symbolic} (${new_octal})${NC}"
    else
        echo -e "  Status          : ${GREEN}COMPLIANT${NC} (No changes needed)"
    fi
    echo ""
}

# ------------------------------------------------------------------------------
# Main Execution Flow
# ------------------------------------------------------------------------------
if [[ "${1:-}" == "--setup-demo" ]]; then
    setup_demo_env
    TARGET_DIR="./projects"
fi

if [[ ! -d "${TARGET_DIR}" ]]; then
    echo -e "${RED}[!] Error: Target directory '${TARGET_DIR}' does not exist.${NC}"
    echo -e "    Tip: Run '$0 --setup-demo' to generate a local test environment."
    exit 1
fi

echo "======================================================================"
echo "1. INITIAL PERMISSIONS AUDIT (ls -la ${TARGET_DIR})"
echo "======================================================================"
ls -la "${TARGET_DIR}"
echo ""

echo "======================================================================"
echo "2. POLICY ENFORCEMENT & REMEDIATION"
echo "======================================================================"

# Task 1: Remove write access for 'other' on project_k.txt
remediate_item \
    "${TARGET_DIR}/project_k.txt" \
    "-rw-rw-r--" \
    "o-w" \
    "No 'other' write permissions allowed on research files."

# Task 2: Make archived hidden file .project_x.txt read-only for user and group
remediate_item \
    "${TARGET_DIR}/.project_x.txt" \
    "-r--r-----" \
    "u-w,g-w,g+r" \
    "Archived hidden files must be read-only for user and group (no write access)."

# Task 3: Restrict drafts directory exclusively to the owner
remediate_item \
    "${TARGET_DIR}/drafts" \
    "drwx------" \
    "g-x" \
    "Only owner (researcher2) may access the drafts directory."

echo "======================================================================"
echo "3. POST-REMEDIATION VERIFICATION (ls -la ${TARGET_DIR})"
echo "======================================================================"
ls -la "${TARGET_DIR}"
echo -e "\n${GREEN}[✓] Audit and permission remediation complete.${NC}"
