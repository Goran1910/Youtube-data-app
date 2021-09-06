import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComboAlbumsComponent } from './combo-albums.component';

describe('ComboAlbumsComponent', () => {
  let component: ComboAlbumsComponent;
  let fixture: ComponentFixture<ComboAlbumsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComboAlbumsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ComboAlbumsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
