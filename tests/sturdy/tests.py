import pytest

from defi.protocols.sturdy.contracts.LendingPool import SturdyLendingPoolContract

from head.bridge.configurator import BridgeConfigurator
from providers.abstracts.fabric import providerAbstractFabric


class TestSturdyLendingPoolContract:

    _address = '0xA422CA380bd70EeF876292839222159E41AAEe17'
    _provider = BridgeConfigurator(abstractFabric=providerAbstractFabric, fabricKey='http', productKey='eth').produceProduct()

    _instance = SturdyLendingPoolContract()\
        .setAddress(address=_address)\
        .setProvider(provider=_provider)\
        .create()

    def testInstance(self):
        assert isinstance(self._instance, SturdyLendingPoolContract)

    def testAddress(self):
        assert self._instance.address == self._address

    def testProvider(self):
        assert self._instance.provider == self._provider

    def test_FLASHLOAN_PREMIUM_TOTAL(self):
        assert isinstance(self._instance.FLASHLOAN_PREMIUM_TOTAL(), int)

    def test_MAX_NUMBER_RESERVES(self):
        assert isinstance(self._instance.MAX_NUMBER_RESERVES(), int)

    def test_MAX_STABLE_RATE_BORROW_SIZE_PERCENT(self):
        assert isinstance(self._instance.MAX_STABLE_RATE_BORROW_SIZE_PERCENT(), int)

    def test_getAddressesProvider(self):
        assert isinstance(self._instance.getAddressesProvider(), str)

    def test_getBorrowingAssetAndVolumes(self):
        assert isinstance(self._instance.getBorrowingAssetAndVolumes(), list)

    def test_getConfiguration(self):
        _asset = '0x0000000000000000000000000000000000000000'
        assert isinstance(self._instance.getConfiguration(asset=_asset), tuple)

    def test_getReserveData(self):
        _asset = '0x0000000000000000000000000000000000000000'
        assert isinstance(self._instance.getReserveData(asset=_asset), tuple)

    def test_getReserveNormalizedIncome(self):
        _asset = '0x0000000000000000000000000000000000000000'
        assert isinstance(self._instance.getReserveNormalizedIncome(asset=_asset), int)

    def test_getReserveNormalizedVariableDebt(self):
        _asset = '0x0000000000000000000000000000000000000000'
        assert isinstance(self._instance.getReserveNormalizedVariableDebt(asset=_asset), int)

    def test_getReservesList(self):
        assert isinstance(self._instance.getReservesList(), list)

    def test_getTotalBalanceOfAssetPair(self):
        _asset = self._instance.getReservesList()[0]
        assert isinstance(self._instance.getTotalBalanceOfAssetPair(asset=_asset), list)

    def test_getUserAccountData(self):
        _address = '0x0000000000000000000000000000000000000000'
        assert isinstance(self._instance.getUserAccountData(address=_address), list)

    def test_getUserConfiguration(self):
        _address = '0x0000000000000000000000000000000000000000'
        assert isinstance(self._instance.getUserConfiguration(address=_address), tuple)

    def test_paused(self):
        assert isinstance(self._instance.paused(), bool)
